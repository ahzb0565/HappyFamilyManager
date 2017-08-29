FINANCIAL_ACCOUNT_TYPE = (
    ('essential', 'Floating capital, expendable found, bank savings etc.'),
    ('safeguard', 'Accident insurance, illness insurance, endowment insurance etc.'),
    ('investment', 'Investment and financing'),
    ('debt', 'Borrow or lend, house loan, car loan, personal loan and so on'),
)

CAPITAL_TYPE = (
    ('cash', 'Floating capital'),
    ('spare', 'Spare founds'),
    ('deposit', 'Bank saving etc.'),
    ('zhifubao', 'Zhifubao or Yuebao'),
)

INSURANCE_TYPE = (
    ('accident', 'Accident insurance'),
    ('health', 'Illness insurance'),
    ('lifespan', 'Illness insurance'),
    ('property', 'Property insurance'),
    ('academic', 'Academic insurance'),
    ('pension', 'Pension'),
    ('vehicle', 'car, trucks insurance etc.'),
)

INVESTMENT_TYPE = (
    ('funds', 'Funds'),
    ('insurance', 'Insurance'),
    ('stock', 'Stock'),
    ('p2p', 'P2P'),
)

FUNDS_TYPE = (
    ('stock', 'Stock funds or stock hybrid funds'),
    ('bond', 'Bond funds or bond hybrid funds'),
    ('hybrid', 'Hybrid funds that include stock and bonds')
)

LEVEL = (
    ('H', 'High'),
    ('L', 'Low'),
    ('M', 'Middle'),
)

DEBT_TYPE = (
    ('borrow', 'Borrow from somebody'),
    ('lend', 'Lend to somebody'),
    ('house_debt', 'House debt'),
    ('car_debt', 'car debt'),
    ('personal', 'personal debt'),
)

STATUS = (
    ('active', 'Active'),
    ('terminated', 'Terminated'),
    ('inactive', 'Inactive'),
)