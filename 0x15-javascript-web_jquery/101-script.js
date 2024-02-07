$(function () {
  const $list = $("ul.my_list");

  $("#add_item").click(function() {
    $list.append('<li>Item</li>');
  });

  $("#remove_item").click(function () {
    $list.children().last().remove();
  });

  $("#clear_list").click(function () {
    $list.children().remove();
  });
});
