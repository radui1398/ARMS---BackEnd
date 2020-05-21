# Instruction

Just run app.py.

### GET TWEETS BY DATE/COUNTRY
http://127.0.0.1:5000/?d=20&y=2020&m=5&country=[country]

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
        time
    }
    
Can fail with 400/404/500.


### GET TWEETS BY COUNTRY FOR TODAY (-1 ACTUALLY)
http://127.0.0.1:5000/today?country=[country]

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

