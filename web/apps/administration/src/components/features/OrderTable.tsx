import { Order } from "@/api";
import { OrderRoutes } from "@/app/routes";
import {
  AddCard as AddCardIcon,
  ShoppingCart as ShoppingCartIcon,
  ConfirmationNumber as TicketIcon,
} from "@mui/icons-material";
import { Link, Tooltip } from "@mui/material";
import { DataGrid, GridColDef, DataGridTitle } from "@stustapay/framework";
import * as React from "react";
import { useTranslation } from "react-i18next";
import { Link as RouterLink } from "react-router-dom";

export interface OrderListProps {
  orders: Order[];
}

const orderTypeToIcon: Record<string, React.ReactElement> = {
  // "cancel_sale":,
  // "money_transfer":,
  // "money_transfer_imbalance":,
  // "pay_out":,
  sale: <ShoppingCartIcon />,
  ticket: <TicketIcon />,
  top_up: <AddCardIcon />,
};

export const OrderTable: React.FC<OrderListProps> = ({ orders }) => {
  const { t } = useTranslation();

  const columns: GridColDef<Order>[] = [
    {
      field: "id",
      headerName: t("order.id"),
      renderCell: (params) => (
        <Link component={RouterLink} to={OrderRoutes.detail(params.row.id)}>
          {params.row.id}
        </Link>
      ),
      width: 100,
    },
    {
      field: "order_type",
      headerName: t("order.type"),
      width: 140,
      renderCell: ({ row }) => {
        const icon = orderTypeToIcon[row.order_type];
        if (icon) {
          return <Tooltip title={row.order_type}>{icon}</Tooltip>;
        }
        return row.order_type;
      },
    },
    {
      field: "payment_method",
      headerName: t("order.paymentMethod"),
      width: 150,
    },
    {
      field: "total_no_tax",
      headerName: t("order.totalNoTax"),
      type: "currency",
      width: 150,
    },
    {
      field: "total_tax",
      headerName: t("order.totalTax"),
      type: "currency",
      width: 100,
    },
    {
      field: "total_price",
      headerName: t("order.totalPrice"),
      type: "currency",
      width: 100,
    },
    {
      field: "booked_at",
      headerName: t("order.bookedAt"),
      type: "dateTime",
      valueGetter: (value) => new Date(value),
      flex: 1,
    },
  ];

  return (
    <DataGrid
      autoHeight
      rows={orders ?? []}
      slots={{ toolbar: () => <DataGridTitle title={t("orders")} /> }}
      columns={columns}
      disableRowSelectionOnClick
      sx={{ p: 1, boxShadow: (theme) => theme.shadows[1] }}
    />
  );
};
