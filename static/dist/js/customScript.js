$('#myTable').on('click', '.clickable-row', function(event) {
  $(this).addClass('active').siblings().removeClass('active');
}); 