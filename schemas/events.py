{"events": {
    335675: {
        # could potentially call this collection "event"
        "meta": {
            "created": "2021-03-26 16:25",
            # not sure if this is the right place for the owner.
            "owner": { entire user document of owner },
            "category": "litter",
            # the id of the chat collection for this event. not sure if this is the right place.
            "chat": 8596
        },
        "status": {
            "finished": false,
            "ongoing": false,
            "full": false,
            "cancelled": false,
        },
        "setting": {
            "event_date": "2021-04-03",
            "start_time": "16:00",
            "end_time": "18:00", 
            "location": [-1.17356, 52.4324]
        },
        "description": {
            "name": "Clifton litter picking",
            "summary": "We'll be collecting litter in Clifton",
            "social": "We'll be heading to the King's arms afterwards!",
            "picture": "www.s3link.com/an-s3-link"
        },
        "parameters": {
            "max_attendance": 10,
            "approval_required": true,
            "forms_required": true,
            # not sure if this should be it's own collection
            # only populated if 335675.paramaters.forms_required = true
            "forms": {
                1: {
                    "form_id": 1,
                    "form_description": "You will need to submit your ID to attend this event",
                    "form_example": "www.s3link.com/an-s3-link"
                }
            }
        },
        "attendance": {
            "current_attendance": 2,
            "attendees": {
                7564: {
                    "attendee": { entire user document of attendee },
                    "attended": false,
                    "documents": {
                        1: "www.s3link.com/an-s3-link"
                    }
                },
                1354: {
                    "attendee": { entire user document of attendee },
                    "attended": false,
                    "documents": {
                        1: "www.s3link.com/an-s3-link"
                    }
                }
            }
        },
        # this will only be populated if 335675.parameters.approval_required = true
        "requests": {
            "current_requests": 1,
            "attendees": {
                7564: {
                    "attendee": { entire user document of attendee },
                    "attended": false,
                    "documents": {
                        1: "www.s3link.com/an-s3-link"
                    }
                },
            }
        }
    }
}}