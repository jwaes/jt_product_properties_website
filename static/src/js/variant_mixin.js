// odoo.define('jt_product_properties_website.VariantMixin', function (require) {
//     'use strict';
    
// const {Markup} = require('web.utils');
// var VariantMixin = require('sale.VariantMixin');
// var publicWidget = require('web.public.widget');

// require('website_sale.website_sale');

import VariantMixin from "@website_sale/js/variant_mixin";


window.addEventListener("load", (event) => {
    console.log("page is fully loaded");
    const $product = $('#product_detail');
});

const originalOnChangeCombination = VariantMixin._onChangeCombination;

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
        // return;
    }
    console.log("updating properties ");

    $('div.product_properties').html(combination.product_properties);
    $('#product_details h5').text(combination.attribute_string);

    originalOnChangeCombination.apply(this, [ev, $parent, combination]);
};

export default VariantMixin;