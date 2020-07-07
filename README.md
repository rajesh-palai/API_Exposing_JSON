# API EXPOSE
Database has been prepopulated using Faker Module
API has been exposed with Two endpoints.

1- one endpoint is to get all the Json data from database and also for post json data into server

    path('user-api/',views.UserListDetailsView.as_view(),name = "listAndCreate")
    
2-another end point is for Retrieve,Update and Delete operation.
    
   path('user-api/<int:pk>/',views.UserRetrieveDeleteUpdateView.as_view(),name = "retrieveUpdateDelete")
   
json data format is given below
    {
        "userInfo_by_user": {
            "ok": true
        },
        "members": [
            {
                "activity_periods": [
                    {
                        "start_time": "2020-07-01T00:00:00Z",
                        "end_time": "2020-07-08T00:00:00Z"
                    },
                    {
                        "start_time": "2020-07-03T06:00:00Z",
                        "end_time": "2020-07-10T18:00:00Z"
                    },
                    {
                        "start_time": "2020-07-02T06:00:00Z",
                        "end_time": "2020-07-16T06:00:00Z"
                    }
                ],
                "member_id": "AZ5CQF",
                "real_name": "chandler Bing",
                "tz": "Africa/Asmara"
            },
            {
                "activity_periods": [
                    {
                        "start_time": "2020-07-02T18:00:00Z",
                        "end_time": "2020-07-17T12:00:00Z"
                    },
                    {
                        "start_time": "2020-07-01T16:37:26Z",
                        "end_time": "2020-07-16T06:00:00Z"
                    },
                    {
                        "start_time": "2020-07-02T06:00:00Z",
                        "end_time": "2020-07-10T06:00:00Z"
                    }
                ],
                "member_id": "AF6CQH",
                "real_name": "monica Geller",
                "tz": "Africa/Conakry"
            }   