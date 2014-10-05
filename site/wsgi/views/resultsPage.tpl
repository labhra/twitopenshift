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
          % s = len(scores)
          % no = 1
          % while (s > 0):
              [ {{no}},  {{ scores[s-1] }} ],
          %   s = s-1
          % no = no+1
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
    
    <div id="mainwrapper">
      <h1>Results for {{ query }}</h1>
    <!--Div that will hold the pie chart-->
    <a class="btn btn-primary btn-large" href="/home">Do another search</a> 
    <div id="topwrapper">
    <div class="smallbox">
      <h2>What does this mean?</h2>
      <p>A SentiScore between 1 and -1 is allocated to each Tweet depending on the sentiment expressed in it, with -1 being totally negative, 0 being neutal, and 1 being totally positive.</p>
      
    </div>
    <div id="chart_div"></div> 
    </div>
    <p></p>
    <div id="chart_div2"></div>
        <p>  {{ results[(len(results) - 1)][7]}} <img src="/static/img/arrow.png" /> {{ results[0][7] }} </p>
        <br />
    
    
    
    
  	% for eachResult in results:
    <article class="{{ eachResult[5] }}">
    <div class="pic">
        <img class="img-rounded" src= "{{ eachResult[4] }}" width="75px" height="75px" />
        </div>
        <div class="name">
        <h2> {{ eachResult[3] }} <small>@{{ eachResult[2] }}</small></h2>  </div>

        <h3> {{ eachResult[0] }} </h3>
        <p> {{eachResult[7]}} SentiScore: {{eachResult[6]}}</p> 

      </article>
      % end
% rebase('layout.tpl', title='Results') #add to layout

  </div>
