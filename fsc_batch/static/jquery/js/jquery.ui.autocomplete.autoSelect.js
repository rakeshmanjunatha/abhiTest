/*
 * jQuery UI Autocomplete Auto Select Extension
 *
 * Copyright 2010, Scott González (http://scottgonzalez.com)
 * Dual licensed under the MIT or GPL Version 2 licenses.
 *
 * http://github.com/scottgonzalez/jquery-ui-extensions
 *
 * 3/15/2017 - @vulugundam Modified to work on recent versions of
 *                          jquery and jquery ui
 * 4/6/2017 - @vulugundam Modified to work for return key press
 *
 */
(function( $ ) {

$.ui.autocomplete.prototype.options.autoSelect = true;
$(document.body).on( "blur keypress", ".ui-autocomplete-input", function( event ) {
    var autocomplete = $( ".ui-autocomplete-input" ).data( "uiAutocomplete" );
    if ( !autocomplete.options.autoSelect || autocomplete.selectedItem ) { return; }

    var matcher = new RegExp( "^" + $.ui.autocomplete.escapeRegex( $(".ui-autocomplete-input").val() ) + "$", "i" );
    autocomplete.widget().children( ".ui-menu-item" ).each(function() {
        var item = $( this ).data( "ui-autocomplete-item" );
        if ( matcher.test( item.label || item.value || item ) ) {
            autocomplete.selectedItem = item;
            return false;
        }
    });
    if ( autocomplete.selectedItem ) {
        autocomplete._trigger( "select", event, { item: autocomplete.selectedItem } );
        if(event.keyCode == 13) {
            autocomplete.widget().hide();
        }
    } else {
        if(event.keyCode == 13) {
            autocomplete._trigger( "change", event, { } );
            event.preventDefault();
        }
    }
});

}( jQuery ));
