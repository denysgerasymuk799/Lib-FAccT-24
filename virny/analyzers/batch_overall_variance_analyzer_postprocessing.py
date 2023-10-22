import numpy as np
import pandas as pd

from tqdm.notebook import tqdm

from virny.analyzers.batch_overall_variance_analyzer import BatchOverallVarianceAnalyzer
from virny.utils.postprocessing_intervention_utils import contruct_binary_label_dataset_from_df, construct_binary_label_dataset_from_samples, predict_on_binary_label_dataset
from virny.utils.stability_utils import generate_bootstrap


class BatchOverallVarianceAnalyzerPostProcessing(BatchOverallVarianceAnalyzer):
    def __init__(self, postprocessor, sensitive_attribute: str, 
                 base_model, base_model_name: str, bootstrap_fraction: float,
                 X_train: pd.DataFrame, y_train: pd.DataFrame, X_test: pd.DataFrame, y_test: pd.DataFrame,
                 target_column: str, dataset_name: str, n_estimators: int, verbose: int = 0):
        super().__init__(base_model=base_model,
                         base_model_name=base_model_name,
                         bootstrap_fraction=bootstrap_fraction,
                         X_train=X_train,
                         y_train=y_train,
                         X_test=X_test,
                         y_test=y_test,
                         target_column=target_column,
                         dataset_name=dataset_name,
                         n_estimators=n_estimators,
                         verbose=verbose)
        
        self.postprocessor = postprocessor
        self.sensitive_attribute = sensitive_attribute
        self.test_binary_label_dataset = contruct_binary_label_dataset_from_df(X_test, y_test, target_column, sensitive_attribute)
        
    def UQ_by_boostrap(self, boostrap_size: int, with_replacement: bool, with_fit: bool = True) -> dict:
        """
        Quantifying uncertainty of the base model by constructing an ensemble from bootstrapped samples
        and applying postprocessing intervention.

        Return a dictionary where keys are models indexes, and values are lists of
         correspondent model predictions for X_test set.

        Parameters
        ----------
        boostrap_size
            Number of records in bootstrap splits
        with_replacement
            Enable replacement or not
        with_fit
            Whether to fit estimators in bootstrap

        """
        models_predictions = {idx: [] for idx in range(self.n_estimators)}
        if self._verbose >= 1:
            print('\n', flush=True)
        self._AbstractOverallVarianceAnalyzer__logger.info('Start classifiers testing by bootstrap')
        # Remove a progress bar for UQ without estimators fitting
        cycle_range = range(self.n_estimators) if with_fit is False else \
            tqdm(range(self.n_estimators),
                 desc="Classifiers testing by bootstrap",
                 colour="blue",
                 mininterval=10)
        # Train and test each estimator in models_predictions
        for idx in cycle_range:
            classifier = self.models_lst[idx]
            if with_fit:
                X_sample, y_sample = generate_bootstrap(self.X_train, self.y_train, boostrap_size, with_replacement)
                classifier = self._fit_model(classifier, X_sample, y_sample)

            train_binary_label_dataset_sample = construct_binary_label_dataset_from_samples(X_sample, y_sample, self.X_train.columns, self.target_column, self.sensitive_attribute)
            train_binary_label_dataset_sample_pred = predict_on_binary_label_dataset(classifier, train_binary_label_dataset_sample)
            test_binary_label_dataset_pred = predict_on_binary_label_dataset(classifier, self.test_binary_label_dataset)
            postprocessor_fitted = self.postprocessor.fit(train_binary_label_dataset_sample, train_binary_label_dataset_sample_pred)
            
            models_predictions[idx] = postprocessor_fitted.predict(test_binary_label_dataset_pred).labels.ravel()
            self.models_lst[idx] = classifier

        if self._verbose >= 1:
            print('\n', flush=True)
        self._AbstractOverallVarianceAnalyzer__logger.info('Successfully tested classifiers by bootstrap')

        return models_predictions
        