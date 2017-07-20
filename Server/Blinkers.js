var dbInfo = require('./dbInfo');

exports.selectBlinkers = function(req, res)
{
    dbInfo.dbConnect.query('call selectLinechange()', function(err, rows, fields)
    {
	var winker1 = rows[0];
	//print->{winker:3}ë
	var winker2 = winker1[0];
	var value = winker2["winker"];
	if(value=='C'){
		res.writeHead(200, {"Content-Type": "text/html"});
		res.end("<h1>Center</h1>");
		//res.json(rows);
	}
	else
	{
		res.json(rows);
	}
    });
};

exports.insertBlinkers = function(req, res)
{
    var twinkerValue = "'"+req.body.Value+"'",
        getTime = "'" + req.body.Time + "'",
        Handle = "'"+req.body.Handle+"'";
 
    var data = ''+getTime+','+twinkerValue+','+Handle+'';
    console.log(data);

    dbInfo.dbConnect.query('call insertHandle('+data+');', function(error,result)
    {
        if(!error)
        {
            console.log("Insert_Finish");
	    res.json("insert_finish");
        }
        else
        {
            res.json("insert_failed");
	    console.log(error);
        } 
    });
};

