$(document).ready(function() {


		$('#calendar').fullCalendar({
			editable: false,
			eventLimit: true, // allow "more" link when too many events
			events: '/calendars'
		});

	
		$('#calendar').fullCalendar('changeView', 'agendaWeek');
		
	});