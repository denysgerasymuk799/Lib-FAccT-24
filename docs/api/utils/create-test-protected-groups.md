# create_test_protected_groups

Create protected groups based on a test feature set. Use a disadvantaged group as a reference group.

Return a dictionary where keys are subgroup names, and values are X_test row indexes correspondent to this subgroup.

## Parameters

- **X_test** (*pandas.core.frame.DataFrame*)

    Test feature set

- **init_features_df** (*pandas.core.frame.DataFrame*)

    Initial full dataset without preprocessing

- **sensitive_attributes_dct** (*dict*)

    A dictionary where keys are sensitive attribute names (including attributes intersections),  and values are disadvantaged values for these attributes




