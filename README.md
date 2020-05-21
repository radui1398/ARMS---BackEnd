# Instruction

Just run app.py.

### GET TWEETS BY DATE/COUNTRY
https://arsm-backend.herokuapp.com/?d=21&y=2020&m=5&country=Romania

    QParams: 
    d = Day
    m = Month
    y = Year
    country = Country
    
    Returns:
    {
        data: [array of tweets]
    }
    
    Tweet structure: 
    {
        id,
        html,
        text,
        url,
        user,
        screen_name,
        time
    }
    
Can fail with 400/404/500.


### GET TWEETS BY COUNTRY FOR TODAY (-1 ACTUALLY)
https://arsm-backend.herokuapp.com/today?country=Romania

    QParams: 
    country = Country
    
    Returns:
    {
        data: [array of tweets]
    }
    
    Tweet structure: 
    {
        id,
        html,
        text,
        url,
        user,
        time
    }
    
Can fail with 400/404/500.

