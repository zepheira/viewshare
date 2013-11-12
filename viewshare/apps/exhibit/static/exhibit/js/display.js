define(["freemix/js/lib/jquery",
        "exhibit/js/views/registry",
        "exhibit/js/facets/registry",
        "exhibit/js/lenses/registry",
        "freemix/js/freemix"],
    function($, ViewRegistry, FacetRegistry, LensRegistry, Freemix) {
    "use strict";

    $.fn.generateExhibitHTML = function(model) {

        return this.each(function() {
            var root = $(this);

            root.find(".view-container").each(function() {
                var id = $(this).attr("id");
                var container = $("<div class='view-panel' data-ex-role='viewPanel'></div>");
                $.each(model.views[id], function() {
                    var view = new ViewRegistry.construct(this.type,this);
                    container.append(view.generateExhibitHTML());
                });

                root.find(".view-container#" + id).append(container);
            });

            $.each(model.facets, function(container, facets) {
                $.each(facets, function() {
                    var facet = FacetRegistry.construct(this.type, this);
                    root.find(".facet-container#" +container).append(facet.generateExhibitHTML());
                });
            });
            $('body').trigger('initialized.exhibit');

        });
    };

    function run_init(profile, nextFn) {
        var data = $("link[rel='exhibit/data']").toArray();
        var url = $("link[rel='exhibit/data']").attr("href");
        $.getJSON(url, function(data) {
            Freemix.exhibit.initializeDatabase(data, function() {
                if (profile.default_lens) {
                    LensRegistry.setDefaultLens(LensRegistry.construct(profile.default_lens));
                }
                $("#canvas").generateExhibitHTML(profile).createExhibit();
            });
            
            if (typeof nextFn != "undefined") {
                nextFn();
            }
        });
    }

    Freemix.initialize = function(callback) {
        var profile_url = $("link[rel='freemix/exhibit_profile']").attr("href");
        $.ajax({
            url: profile_url,
            type: "GET",
            dataType: "json",
            success: function(p) {
                run_init(p,callback);
            }
        });


    };


});
