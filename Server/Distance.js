var dbInfo = require('./dbInfo');

exports.selectDistance = function(req, res)
{
    dbInfo.dbConnect.query('call selectDistance()', function(err, rows, fields)
    {
        res.json(rows);
        console.log("Select Distance");
    });
};

exports.insertDistance = function(req, res)
{
    console.log(req.body);
    var frontValue = req.body.frontValue,
        rightValue = req.body.rightValue,
        leftValue = req.body.leftValue,  
        getTime = "'" + req.body.checkTime + "'";
 
    var data = ''+getTime+','+frontValue+','+rightValue+','+leftValue+'';
    console.log(data);

    dbInfo.dbConnect.query('call insertDistance('+data+');', function(error,result)
    {
        if(!error)
        {
            res.json("insert_finish");
        }
        else
        {
            console.log(error);
            res.json("insert_failed");
        } 
    });
};

