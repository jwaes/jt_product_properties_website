odoo.define('jt_product_properties_website.VariantMixin', function (require) {
    'use strict';

    
const {Markup} = require('web.utils');
var VariantMixin = require('sale.VariantMixin');
var publicWidget = require('web.public.widget');
var ajax = require('web.ajax');
var core = require('web.core');
var QWeb = core.qweb;

const loadXml = async () => {
    return ajax.loadXML('/jt_product_properties_website/static/src/xml/website_sale_product_properties.xml', QWeb);
};

require('website_sale.website_sale');

/**
 * Addition to the variant_mixin._onChangeCombination
 *
 * This will prevent the user from selecting a quantity that is not available in the
 * stock for that product.
 *
 * It will also display various info/warning messages regarding the select product's stock.
 *
 * This behavior is only applied for the web shop (and not on the SO form)
 * and only for the main product.
 *
 * @param {MouseEvent} ev
 * @param {$.Element} $parent
 * @param {Array} combination
 */
VariantMixin._onChangeCombinationProductProperties = function (ev, $parent, combination) {
    let product_id = 0;
    // needed for list view of variants
    if ($parent.find('input.product_id:checked').length) {
        product_id = $parent.find('input.product_id:checked').val();
    } else {
        product_id = $parent.find('.product_id').val();
    }
    const isMainProduct = combination.product_id &&
        ($parent.is('.js_main_product') || $parent.is('.main_product')) &&
        combination.product_id === parseInt(product_id);

    if (!this.isWebsite || !isMainProduct) {
        return;
    }

    const $addQtyInput = $parent.find('input[name="add_qty"]');
    let qty = $addQtyInput.val();

    console.debug("here comes combination")
    console.debug(combination)

    loadXml().then(function (result) {
        $('.oe_website_sale')
            .find('.availability_message_' + combination.product_template)
            .remove();
        combination.product_properties = Markup(combination.product_properties);
        const $message = $(QWeb.render(
            'jt_product_properties_website.product_properties',
            combination
        ));
        $('div.product_properties').html($message);
    });
};

publicWidget.registry.WebsiteSale.include({
    /**
     * Adds the product properties updating to the regular _onChangeCombination method
     * @override
     */
    _onChangeCombination: function () {
        this._super.apply(this, arguments);
        VariantMixin._onChangeCombinationProductProperties.apply(this, arguments);
    },
    /**
     * Recomputes the combination after adding a product to the cart
     * @override
     */
    _onClickAdd(ev) {
        return this._super.apply(this, arguments).then(() => {
            if ($('div.availability_messages').length) {
                this._getCombinationInfo(ev);
            }
        });
    }
});

return VariantMixin;

});