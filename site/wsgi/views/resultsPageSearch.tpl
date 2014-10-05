<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.1.1/css/bootstrap-combined.min.css" rel="stylesheet">
    <title>Results</title>
    <style type="text/css">
    body {
          background-color: :#000; 
    }
    article {
          border: 3px solid;
          margin: 15px;
          padding: 15px;
          padding-bottom:20px;
          font-family: Arial, Helvetica, sans-serif;
          font-weight: bold;
          border-radius: 10px;
    }
    .positive{
          background-color: #0C6;
    }

    .negative {
        background-color: #C03;
    }

    .neutral  {
          background-color: #CCC;
    }

    .name {
          display: inline-block;
    }

    .pic  {
          display: inline-block;
    }
    

    </style>

    <script type='text/javascript' src='https://www.google.com/jsapi'></script>
    <script type='text/javascript'>

      google.load('visualization', '1', {packages:['corechart']});

      google.setOnLoadCallback(drawChart);
      google.setOnLoadCallback(drawChart2);
      
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
          ['Sentiment', 'Value'],
          ['Positive', {{ breakdown[0] }} ],
          ['Negative', {{ breakdown[1] }} ],
          ['Neutral', {{ breakdown[2] }} ]
        ]);

        // Set chart options
        var options = {'title':'Sentiment Analysis of Tweets',
                       'width':400,
                       'height':300,
                       'colors': ['#0C6', '#C03', '#CCC'],
                       'border': 2,
                      }

        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        chart.draw(data, options);      
      }    

      function drawChart2() {
        var data = new google.visualization.arrayToDataTable([
          ['Result Number', 'Sentiment Analysis of Tweet'],
          % s = 0
          % while (s < len(scores)):
              [ {{s+1}},  {{ scores[s] }} ],
          %   s = s+1
          % end
        ]);

        
        var options = {
          title: 'Sentiment Analysis of Tweets'
        };


        // Instantiate and draw our chart, passing in some options.
        

       var chart = new google.visualization.LineChart(document.getElementById('chart_div2'));
        chart.draw(data, options);
      }
    </script>
    

  </head>
  <body>
    <div class="container">
      <h1>Results for {{ query }} from {{resultType}} Tweets</h1>
      <div class="navbar">
              <div class="navbar-inner">
                <div class="container">
                  <ul class="nav">
                    <li><a href="/home">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/contact">Contact</a></li>
                  </ul>
                </div>
              </div>
            </div>
    <!--Div that will hold the pie chart-->
    <div id="chart_div"></div> 
    <p></p>
    <div id="chart_div2" width="550px" height="500px"></div> 
    
    
  	% for eachResult in results:
    <article class= {{ eachResult[5] }}>
    <div class="pic">
        <img class="img-rounded" src= "{{ eachResult[4] }}" width="75px" height="75px" />
        </div>
        <div class="name">
        <h2> {{ eachResult[3] }} <small>@{{ eachResult[2] }}</small></h2>  </div>

        <h3> {{ eachResult[0] }} </h3>
        <p> {{eachResult[7]}} SentiScore: {{eachResult[6]}}</p> 

      </article>
      % end

      <!-- pic, time, link? graaaaaaph? 
      geocode parameter specified with the template "latitude,longitude,radius", for example, "37.781157,-122.398720,1mi
      until
optional
Returns tweets generated before the given date. Date should be formatted as YYYY-MM-DD. Keep in mind that the search index may not go back as far as the date you specify here.
      "-->

      
      <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
      <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.1.1/js/bootstrap.min.js"></script>

  </body>
</html>

