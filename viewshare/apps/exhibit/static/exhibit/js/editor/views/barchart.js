define(["jquery",
        "exhibit/js/views/barchart",
        "ext/flot/scripts/barchart-view"],
        function ($, View, BarChartView) {
        "use strict"

    View.prototype.label = "Bar Chart";
    View.prototype.thumbnail = "/static/exhibit/img/piechart-icon.png";

    View.prototype.viewClass = BarChartView;
    View.prototype.template_name = "barchart-view-template";

    // Display the view's UI.
    View.prototype.setupEditor = function(config, template) {
        this._setupViewForm(config, template);
        this._setupLabelEditor(config, template);
        var props = Freemix.exhibit.database.getAllPropertyObjects();

        var property_list = template.find("#property_list");
        //this._setupPropertyMultiSelect(config, template, property_list, "properties", true);
        this._setupPropertySelect(config, template, property_list, "grouping", props)
        property_list.change();

        this._setupLensEditor(config, template);

    };
    return View;
});