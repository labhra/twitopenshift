    <script type='text/javascript' src='https://www.google.com/jsapi'></script>
    <script type='text/javascript'>

      google.load('visualization', '1', {packages:['corechart']});

      
      google.setOnLoadCallback(drawChart2);
      

      function drawChart2() {
        var data = new google.visualization.arrayToDataTable([
          ['Date', 'Sentiment Analysis of Tweet'],
          % s = len(results)
          % no = 1
          % while (s > 0):
              [ '{{ results[s-1][1] }}',  {{ results[s-1][0] }} ],
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
    <div id="chart_div2"></div>
        <p>  {{ results[(len(results) - 1)][1]}} <img src="/static/img/arrow.png" /> {{ results[0][1] }} </p>
        <br />
    <div class="homebox">
    <h2>What is this?</h2>
    <p>On this page we've decided to keep track of a particular search term pulling 100 tweets about it every day, this month's term is Dublin to see how people are enjoying their summer holidays here!</p>
    <p>For suggestions for future terms, tweet me @labhra89</p>
    </div>

    <div class="smallbox">
      <h2>What does this mean?</h2>
      <p>A SentiScore between 1 and -1 is allocated to each Tweet depending on the sentiment expressed in it, with -1 being totally negative, 0 being neutal, and 1 being totally positive.</p>
    </div>
    

% rebase('layout.tpl', title='Timeline') #add to layout

  </div>
