#!/usr/bin/node
$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    data.results.forEach(function (i) {
      $('UL#list_movies').append(`<li>${i.title}</li>`);
    });
  });
});
