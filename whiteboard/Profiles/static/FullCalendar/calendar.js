$(document).ready(function() {


		$('#calendar').fullCalendar({
			editable: false,
			allDaySlot: false,
			scrollTime: '08:00:00',
			slotDuration: '00:20:00',
			slotLabelInterval: '00:30:00',
			header: false,
			columnFormat: 'dddd',
			dayNames: ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday'],
			eventLimit: true, // allow "more" link when too many events
			events: '/calendars'
		});

	
		$('#calendar').fullCalendar('changeView', 'agendaWeek');
		
	});