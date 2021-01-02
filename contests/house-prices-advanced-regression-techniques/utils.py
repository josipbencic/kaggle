# Columns that are already numerical
numerical_columns = [
      '1stFlrSF',
      '2ndFlrSF',
      '3SsnPorch',
      'BedroomAbvGr',
      'BsmtFullBath',
      'BsmtHalfBath',
      'EnclosedPorch',
      'Fireplaces',
      'FullBath',
      'GarageArea',
      'GarageCars',
      'GrLivArea',
      'HalfBath',
      'KitchenAbvGr',
      'LotArea',
      'LowQualFinSF',
      'MiscVal',
      'OpenPorchSF',
      'OverallCond',
      'OverallQual',
      'PoolArea',
      'ScreenPorch',
      'TotalBsmtSF',
      'TotRmsAbvGrd',
      'WoodDeckSF',
      'YearBuilt',
      'YearRemodAdd',
      'SalePrice',
]

## need to address the NaN issue
numerical_columns_with_nans = [
  'GarageYrBlt',
  'LotFrontage',
  'MasVnrArea',
]