define(["jquery",
        "exhibit",
        "display/facets/base",
        "freemix/js/freemix",
        "display/facets/registry",
        "layout/widget_editor",
        "text!templates/layout/facet-widget.html",
        "freemix/js/exhibit_utilities"],
    function($, Exhibit, BaseFacet, Freemix, FacetRegistry, WidgetEditor, facet_widget_template) {
    "use strict";

    var expression = function(property){return "." + property;};

    BaseFacet.prototype.refreshEvent = "refresh-preview.facet";


    BaseFacet.prototype.exhibitClass = Exhibit.ListFacet;

    BaseFacet.prototype.findContainer = function() {
        return this.findWidget().parents(".facet-container").data("model");
    };
    BaseFacet.prototype.generateWidget = function() {
        var facet = this;
        return $(facet_widget_template)
                .attr("id", this.config.id)
                .find("span.view-label").text(this.label).end()
                .data("model", this)
                .find(".delete-button").click(function() {
                        facet.remove();
                        return false;
                    }).end()
                .find(".facet-menu a").click(function() {
                        var editor = new WidgetEditor({
                            "title": "Add Widget",
                            "registry": FacetRegistry,
                            "element": facet.findContainer().dialog,
                            "switchable": false,
                            "model": facet
                        });

                        facet.findContainer().dialog.empty().one("shown", function() {
                            editor.render();
                        });

                        facet.findContainer().dialog.modal("show");
                        facet.findContainer().dialog.one("edit-widget", function() {
                            facet.findContainer().dialog.modal("hide");
                            facet.refresh();
                        });
                        facet.findContainer().dialog.off("hidden").one("hidden", function(evt) {
                            editor.destroy();
                        });

                        return false;
                    }).end();

    };

    BaseFacet.prototype.refresh = function() {
        this.findWidget().find(".facet-content").empty().append(this.generateExhibitHTML());
        var exhibit = Freemix.getBuilderExhibit();
        this.exhibitClass.createFromDOM(this.findWidget().find(".facet-content div").get(0), null, exhibit.getUIContext());
    };


    BaseFacet.prototype.showEditor = function(template){
        var model = this;
        var config = $.extend(true, {}, model.config);
        var form = $(this.template());
        template.find(".widget-edit-settings-body").empty().append(form);
        template.off(this.refreshEvent);

        form.submit(function() {return false;});

        this.setupEditor(config, template);

        template.find("#widget_save_button").off("click").click(function() {
           model.config = config;
           template.trigger("edit-widget");
        });
        template.bind(this.refreshEvent, function() {
            model.updatePreview(template.find(".widget-preview-body"), config);

            if (model.errors.length == 0) {
                template.find("#widget_save_button").removeAttr("disabled").removeClass("disabled");
            } else {
                template.find("#widget_save_button").attr("disabled", "disabled").addClass("disabled");
            }
        });
        this.triggerChange(config, template);
    };

    BaseFacet.prototype._propertyRenderer = function(prop) {
        return "." + prop.getID();
    };

    return BaseFacet;

});
