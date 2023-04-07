from odoo import http
from odoo.addons.portal.controllers.portal import CustomerPortal, pager


class MyShopController(CustomerPortal):

    def _prepare_home_portal_values(self, counters):
        counts = super(MyShopController, self)._prepare_home_portal_values(counters)
        counts['item_counts'] = http.request.env['my_module.item'].search_count([])
        return counts

    @http.route(['/my/shop_items', '/my/shop_items/page/<int:page>'], type='http', website=True, auth='public')
    def shop_items_list_view(self, page=1, **kwargs):
        item_obj = http.request.env['my_module.item']
        items_total = item_obj.search_count([])
        page_detail = pager(url='/my/shop_items',
                            total=items_total,
                            page=page,
                            step=5)
        items = item_obj.search([], limit=5, offset=page_detail['offset'])
        context = {'items': items,
                   'page_name': 'items_list',
                   'pager': page_detail}
        return http.request.render('my_module.shop_items_list', context)

