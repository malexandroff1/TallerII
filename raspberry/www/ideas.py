{% for key, value in result.items() %}
         
<td>{{ key }}</td>
<td>{{ value }}</td>

{% endfor %}


@app.route('/thankyou')
def thankyou():
    db = get_db()
    summary_cursor = db.execute('SELECT * FROM orders JOIN order_items USING (transaction_id) WHERE orders.transaction_id = (SELECT MAX(transaction_id) FROM orders)')
    summary = summary_cursor.fetchall()
    data = map(list, summary)
    print data
    if request.args['type'] == 'json':
        return jsonify(summary = data)
    else:
        return render_template('thankyou.html', summary=data))

 <script type=text/javascript>
      $(document).ready(function() {
      
          //sbtn is id of submit button
          $('#btnsubmita').click(function(event) {
            /* Act on the event */
            $.ajax({
              url: '/result', //server url
              type: 'POST',    //passing data as post method
              dataType: 'json', // returning data as json
              data: {a:$('#period').val()},  //form values
              success:function(json)
              {
                alert(json.result);  //response from the server given as alert message

              }
            
            });
            
          });
        });
    </script>


   for (x in counts) {
	            txt +=  + counts[x].temp + '<br>';
	        }
if (period > 0){
			//var refresh = $('meta[name=refresh]').attr("content",period);
			$('head').append('<meta http-equiv="refresh" content=' + 100 + ' />');
		}

window.setInterval(reloadPage(10000), 10000);
		
alert(period);
<meta http-equiv="refresh" content="30">

function reloadPage(time){
	var url = "http://192.168.99.100:8888/result.html";
	var url = window.location.href;    
	
	url += '?period=' + period;
	
	window.location.href = url;

}