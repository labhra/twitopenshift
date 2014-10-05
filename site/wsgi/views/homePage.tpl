    <div class="hero-unit">
      <h2>About</h2>
      <p>Check out what's going on in the world of Twitter about your favourite brands or people.</p>
      <p>Use the find function to go back in time, and the stream function to go forward.</p>
      <p>Their sentiment is calculated from -1 to 1, with -1 being most negative, 0 being neutral and 1 being most positive</p>
      <p>
    <a class="btn btn-primary btn-large" href="/about">Learn more</a>&nbsp;&nbsp;&nbsp;<a class="btn btn-primary btn-large" href="/timeline">Check out our timeline</a></p>
    </div>

        <div class="homebox">
          <h2>Find me the last</h2>
            <form action="/resultsSearch" method="post">
            <input type="radio" name="searchMaxnum" value="3" checked="checked">3 
            <input type="radio" name="searchMaxnum" value="10">10 
            <input type="radio" name="searchMaxnum" value="20">20 
            <input type="radio" name="searchMaxnum" value="50">50  </formbr />
            <input type="radio" name="resulttype" value="recent" checked="checked">recent or
            <input type="radio" name="resulttype" value="popular">popular Tweets
            <h3>from the last</h3>
            <select name="days" required="yes">
              <option value="1">1 day</option>
              <option value="2">2 days</option>
              <option value="3">3 days</option>
              <option value="4">4 days</option>
              <option value="5">5 days</option>
            </select><br />
            <input name="searchSearch" type="text" value="#about" maxlength="25" /><br />
            <input name="searchFind" type="submit" value="Go" /></form>
        </div>

      <div class="homebox">
        <h2>Stream me the next</h2>
          <form action="/resultsStream" method="post">
          <input type="radio" name="streamMaxnum" value="3" checked="checked">3 <br />
          <input type="radio" name="streamMaxnum" value="10">10 <br />
          <input type="radio" name="streamMaxnum" value="20">20 <br />
          <input type="radio" name="streamMaxnum" value="50">50 Tweets  <br /><br />
          <input name="streamSearch" type="text" value="#about" maxlength="25" /><br /><br />
          <input name="streamFind" type="submit" value="Go" /></form>
      </div>
    
  %rebase layout title='Home'