import os
import yaml
import pandas as pd
from munch import DefaultMunch

from virny.utils.common_helpers import validate_config
from virny.configs.constants import INTERSECTION_SIGN


def create_config_obj(config_yaml_path: str):
    """
    Return a config object created based on a config yaml file.

    Parameters
    ----------
    config_yaml_path
        Path to a config yaml file

    """
    with open(config_yaml_path) as f:
        config_dct = yaml.load(f, Loader=yaml.FullLoader)

    config_obj = DefaultMunch.fromDict(config_dct)
    validate_config(config_obj)

    # Fix formatting
    sensitive_attributes_dct_keys = list(config_obj.sensitive_attributes_dct.keys())
    for attr in sensitive_attributes_dct_keys:
        if INTERSECTION_SIGN in attr:
            attrs = attr.strip().split(INTERSECTION_SIGN)
            cleaned_attr = INTERSECTION_SIGN.join(attr.strip() for attr in attrs)
            config_obj.sensitive_attributes_dct[cleaned_attr] = config_obj.sensitive_attributes_dct[attr]

            del config_obj.sensitive_attributes_dct[attr]

    return config_obj


def read_model_metric_dfs(metrics_path, model_names):
    # Read models metrics dfs
    metrics_filenames = [filename for filename in os.listdir(metrics_path)]
    models_metrics_dct = dict()
    for model_name in model_names:
        for filename in metrics_filenames:
            if model_name in filename:
                models_metrics_dct[model_name] = pd.read_csv(f'{metrics_path}/{filename}')
                break

    return models_metrics_dct


def create_models_config_from_tuned_params_df(models_config_for_tuning: dict, tuned_params_df_path: str):
    models_tuned_params_df = pd.read_csv(tuned_params_df_path)
    experiment_models_config = dict()
    for model_name, model_params in models_config_for_tuning.items():
        base_model = create_tuned_base_model(model_params['model'], model_name, models_tuned_params_df)
        experiment_models_config[model_name] = base_model

    return experiment_models_config


def create_tuned_base_model(init_model, model_name, models_tuned_params_df):
    model_params = eval(models_tuned_params_df.loc[models_tuned_params_df['Model_Name'] == model_name,
                                                   'Model_Best_Params'].iloc[0])
    return init_model.set_params(**model_params)
