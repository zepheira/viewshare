/*global define */
define([
       'handlebars',
       'jquery',
       'models/record-collection',
       'views/notification-view',
       'views/record-view',
       'text!templates/editor.html'],
       function (
         Handlebars,
         $,
         RecordCollection,
         NotificationView,
         RecordView,
         editorTemplate) {
  'use strict';
  /**
   * High-level view of records that have properties that can be edited
   * @constructor
   * @param {string} options.model - instance of a RecordCollection
   * @param {object} options.$el - container Element object for this view
   */
  var EditorView = function(options) {
    this.initialize.apply(this, [options]);
  };

  $.extend(EditorView.prototype, {
    initialize: function(options) {
      this.model = options.model;
      this.$el = options.$el;
      this.notificationView = new NotificationView({$el: undefined});
      this.model.Observer('loadSuccess').subscribe(this.render.bind(this));
      this.model.Observer('changeCurrentRecord').subscribe(
        this.changeCurrentRecordNumber.bind(this)
      );
      // bind 'this' to template variables
      this.currentRecordNumber.bind(this);
      this.totalRecords.bind(this);
    },

    /** Compile the template we will use to render the View */
    template: Handlebars.compile(editorTemplate),

    /** Add this view to the DOM */
    render: function() {
      var nextRecord, prevRecord, save;
      // display EditorView
      this.$el.html(this.template(this));
      // assign element to NotificationView for notification display
      this.notificationView.$el = this.$el.find('#notifications');
      // bind to DOM actions
      prevRecord = this.$el.find('#prev-record');
      prevRecord.on('click', this.renderPreviousRecord.bind(this));
      nextRecord = this.$el.find('#next-record');
      nextRecord.on('click', this.renderNextRecord.bind(this));
      save = this.$el.find('#save_button');
      save.on('click', this.model.save.bind(this.model));
      this.renderChildrenViews.apply(this, arguments);
    },

    renderChildrenViews: function() {
      var recordView;
      // display RecordView
      recordView = new RecordView({
        model: this.model.currentRecord(),
        $el: this.$el.find('#records')});
      recordView.render.apply(recordView);
      // display notifications on record actions
      this.notificationView.addSubscription(
        recordView.augmentModal.newProperty,
        'syncSuccess',
        'success',
        'New data has been created which you can use in your views.',
        'Property created successfully!');
    },

    changeCurrentRecordNumber: function() {
      var current = this.$el.find('#current-record-number');
      current.html(this.currentRecordNumber());
    },

    /** Returns current record number for easy templating */
    currentRecordNumber: function() { return this.model._currentRecord + 1; },

    /** Shortcut to EditoryView._currentRecord for easy templating */
    totalRecords: function() { return this.model.records.length; },

    /** Event handler to display the previous record */
    renderPreviousRecord: function(event) {
      this.model.changeCurrentRecord(-1);
      this.renderChildrenViews();
      return false;
    },

    /** Event handler to display the previous record */
    renderNextRecord: function(event) {
      this.model.changeCurrentRecord(1);
      this.renderChildrenViews();
      return false;
    }
  });



  return EditorView;
});
