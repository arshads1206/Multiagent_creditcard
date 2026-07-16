from pydantic import BaseModel
from typing import List


class UserQuery(BaseModel):
    query: str


class Requirement(BaseModel):

    monthly_income: int

    monthly_spend: int

    dining: int

    shopping: int

    groceries: int

    fuel: int

    travel: int

    online: int

    utilities: int

    existing_cards: List[str]

    goal: str

    annual_fee_preference: str

    lifestyle: str

    preferred_bank: str

    credit_score: int

    airport_lounge: bool

    international_usage: bool


class CreditCard(BaseModel):

    name: str

    issuer: str

    annual_fee: str

    joining_fee: str

    reward_type: str

    cashback_rate: str

    dining_benefit: str

    travel_benefit: str

    fuel_benefit: str

    lounge_access: str

    welcome_bonus: str


class EvaluatedCard(CreditCard):

    score: int

    yearly_value: str

    pros: List[str]

    cons: List[str]


class Recommendation(BaseModel):

    recommendation: str

    confidence: int

    expected_yearly_savings: str

    report: str