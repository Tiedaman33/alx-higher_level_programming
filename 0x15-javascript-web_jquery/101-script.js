$(document).ready(function() {
    const $addItem = $('#add_item');
    const $removeItem = $('#remove_item');
    const $clearList = $('#clear_list');
    const $list = $('ul.my_list');

    $addItem.click(function() {
        $list.append('<li>Item</li>');
    });

    $removeItem.click(function() {
        $list.children().last().remove();
    });

    $clearList.click(function() {
        $list.empty();
    });
});
