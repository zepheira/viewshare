(function ($, Freemix) {
    "use strict";

    var Facet = Freemix.facet.prototypes.text;

    Facet.prototype.thumbnail = "/static/exhibit/img/text-facet.png";
    Facet.prototype.label = "Text";
    Facet.prototype.template_name="text-facet-editor";

    Facet.prototype.refresh = function () {
        var facet = this;
        var result = $("<div class='text-facet-content'></div>");
        result.append(this.generateExhibitHTML());
        this.findWidget().find(".facet-content").empty().append(result);
        return result;
    };

    Facet.prototype.setupEditor = function(config, template) {
        var facet = this;
        $("textarea", template)
            .val(config.text || "")
            .keyup(function () {
                config.text = $(this).val();
                template.trigger("update-preview");
            });
    };

    Facet.prototype.updatePreview = function(target, config) {
        config = config || this.config;
        target.empty().creole(config.text);
    };

})(window.Freemix.jQuery, window.Freemix);
