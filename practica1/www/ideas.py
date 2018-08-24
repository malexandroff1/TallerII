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