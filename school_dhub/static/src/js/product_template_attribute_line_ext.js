/** @odoo-module **/

import { ProductTemplateAttributeLine } from "@sale_product_configurator/js/product_template_attribute_line/product_template_attribute_line";
import { patch } from "@web/core/utils/patch";

patch(ProductTemplateAttributeLine.prototype, {
    template:"school_dhub.ptal",
    props : {
        ...ProductTemplateAttributeLine.props,
        attribute: {
            ...ProductTemplateAttributeLine.props.attribute,
            shape: {
                ...ProductTemplateAttributeLine.props.attribute.shape,
                display_type: {
                    type: String,
                    validate: (type) =>
                        ["color", "multi", "pills", "radio", "select", "calendar"].includes(type),
                },
            },
        },
    },

    getPTAVTemplate() {
        switch (this.props.attribute.display_type) {
            case "color":
                return "saleProductConfigurator.ptav-color";
            case "multi":
                return "saleProductConfigurator.ptav-multi";
            case "pills":
                return "saleProductConfigurator.ptav-pills";
            case "radio":
                return "saleProductConfigurator.ptav-radio";
            case "select":
                return "saleProductConfigurator.ptav-select";
            case "calendar":
                return "school_dhub.ptav-date"; // Use your custom module's template
        }
    }
});
