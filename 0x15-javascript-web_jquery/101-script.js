#!/usr/bin/node
$(function () {
  $('DIV#add_item').click(function () {
    $('<li>Item</li>').appendTo('UL.my_list');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list li:last').remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
