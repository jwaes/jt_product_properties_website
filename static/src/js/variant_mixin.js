/** @odoo-module **/

import VariantMixin from "@website_sale/js/variant_mixin";
import publicWidget from "@web/legacy/js/public/public_widget";

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
    $('#product_details h5:first').text(combination.attribute_string);

};

publicWidget.registry.WebsiteSale.include({
    /**
     * Adds the vat to the regular _onChangeCombination method
     * @override
     */
    _onChangeCombination: function () {
        this._super.apply(this, arguments);
        VariantMixin._onChangeCombinationProductProperties.apply(this, arguments);
    },
});

export default VariantMixin;