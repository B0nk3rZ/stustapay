from fastapi import APIRouter
from pydantic import BaseModel

from stustapay.core.http.auth_user import CurrentAuthToken
from stustapay.core.http.context import ContextAccountService
from stustapay.core.http.normalize_data import NormalizedList, normalize_list
from stustapay.core.schema.account import Account
from stustapay.core.service.account import MoneyOverview

router = APIRouter(
    prefix="",
    tags=["accounts"],
    responses={404: {"description": "Not found"}},
)


@router.get("/system-accounts", response_model=NormalizedList[Account, int])
async def list_system_accounts(token: CurrentAuthToken, account_service: ContextAccountService, node_id: int):
    return normalize_list(await account_service.list_system_accounts(token=token, node_id=node_id))


@router.get("/money-overview", response_model=MoneyOverview)
async def get_money_overview(token: CurrentAuthToken, account_service: ContextAccountService, node_id: int):
    return await account_service.get_money_overview(token=token, node_id=node_id)


class FindAccountPayload(BaseModel):
    search_term: str


@router.post("/accounts/find-accounts", response_model=NormalizedList[Account, int])
async def find_accounts(
    token: CurrentAuthToken,
    account_service: ContextAccountService,
    payload: FindAccountPayload,
    node_id: int,
):
    return normalize_list(
        await account_service.find_accounts(token=token, search_term=payload.search_term, node_id=node_id)
    )


@router.get("/accounts/{account_id}", response_model=Account)
async def get_account(token: CurrentAuthToken, account_service: ContextAccountService, account_id: int, node_id: int):
    return await account_service.get_account(token=token, account_id=account_id, node_id=node_id)


@router.post("/accounts/{account_id}/disable")
async def disable_account(
    token: CurrentAuthToken, account_service: ContextAccountService, account_id: int, node_id: int
):
    await account_service.disable_account(token=token, account_id=account_id, node_id=node_id)


class UpdateBalancePayload(BaseModel):
    new_balance: float


@router.post("/accounts/{account_id}/update-balance")
async def update_balance(
    token: CurrentAuthToken,
    account_service: ContextAccountService,
    account_id: int,
    payload: UpdateBalancePayload,
    node_id: int,
):
    await account_service.update_account_balance(
        token=token, account_id=account_id, new_balance=payload.new_balance, node_id=node_id
    )


class UpdateVoucherAmountPayload(BaseModel):
    new_voucher_amount: int


@router.post("/accounts/{account_id}/update-voucher-amount")
async def update_voucher_amount(
    token: CurrentAuthToken,
    account_service: ContextAccountService,
    account_id: int,
    payload: UpdateVoucherAmountPayload,
    node_id: int,
):
    await account_service.update_account_vouchers(
        token=token, account_id=account_id, new_voucher_amount=payload.new_voucher_amount, node_id=node_id
    )


class UpdateAccountCommentPayload(BaseModel):
    comment: str


@router.post("/accounts/{account_id}/update-comment", response_model=Account)
async def update_account_comment(
    token: CurrentAuthToken,
    account_service: ContextAccountService,
    account_id: int,
    payload: UpdateAccountCommentPayload,
    node_id: int,
):
    return await account_service.update_account_comment(
        token=token, account_id=account_id, comment=payload.comment, node_id=node_id
    )
