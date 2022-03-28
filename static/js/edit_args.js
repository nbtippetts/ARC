$('#editScheduleModal').on('show.bs.modal', function (event) {
	var button = $(event.relatedTarget) // Button that triggered the modal
	var recipient = button.data('whatever') // Extract info from data-* attributes
	console.log(recipient)
	// If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
	// Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
	var modal = $(this)
	modal.find('.modal-title').text('New message to ' + recipient)
	modal.find('.modal-body input').val(recipient)
})

var climateModal = document.getElementById('editClimateModal')
climateModal.addEventListener('show.bs.modal', function (event) {
	// Button that triggered the modal
	var button = event.relatedTarget
	// Extract info from data-* attributes
	var recipient = button.getAttribute('data-whatever')
	// If necessary, you could initiate an AJAX request here
	// and then do the updating in a callback.
	//
	// Update the modal's content.
	var modalTitle = climateModal.querySelector('.modal-title')
	var modalBodyInput = climateModal.querySelector('.modal-body form')
	console.log(recipient)
	console.log(modalTitle)
	modalTitle.textContent = 'New message to ' + recipient
	modalBodyInput.setAttribute('action', recipient);
	console.log(modalBodyInput)
})
var intervalModal = document.getElementById('editIntervalModal')
intervalModal.addEventListener('show.bs.modal', function (event) {
	// Button that triggered the modal
	var button = event.relatedTarget
	// Extract info from data-* attributes
	var recipient = button.getAttribute('data-whatever')
	// If necessary, you could initiate an AJAX request here
	// and then do the updating in a callback.
	//
	// Update the modal's content.
	var modalTitle = intervalModal.querySelector('.modal-title')
	var modalBodyInput = intervalModal.querySelector('.modal-body form')
	console.log(recipient)
	console.log(modalTitle)
	modalTitle.textContent = 'New message to ' + recipient
	modalBodyInput.setAttribute('action', recipient);
	console.log(modalBodyInput)
})
// Select/Deselect checkboxes
var checkbox = $('table tbody input[type="checkbox"]');
$("#selectAll").click(function () {
	if (this.checked) {
		checkbox.each(function () {
			this.checked = true;
		});
	} else {
		checkbox.each(function () {
			this.checked = false;
		});
	}
});
checkbox.click(function () {
	if (!this.checked) {
		$("#selectAll").prop("checked", false);
	}
});