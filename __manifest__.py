# Copyright 2021 Camptocamp SA
# comentarios
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Success level",
    "summary": "Puntua el nivel de satisfaccion de un proveedor",
    "version": "15.0.1.0.0",
    "author": "MisaelVz_Estrasol",
    "website": "",
    "category": "Purchase",
    "depends": ["purchase","base","sale","product"],
    "data": [
        "security/ir.model.access.csv",
        "views/success_level_view.xml",
        "views/menus.xml",
        "views/sale_order.xml",
        "views/partner_view.xml",
        "wizard/product_price_view.xml"
    ],
    "license": "AGPL-3",
    "installable": True,
    "application": False,
}
