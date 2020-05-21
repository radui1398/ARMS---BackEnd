# Instruction

Just run app.py.

### GET TWEETS
http://127.0.0.1:5000/?d=20&y=2020&m=5

    QParams: 
    d = day
    m = month
    y = year
    
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