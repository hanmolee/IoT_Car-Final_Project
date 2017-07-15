package com.example.yoon.car_in_us;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends Activity {

    Button bpm_btn;
    public static final int MainActivity = 1111;


    private String result;

    private int a = 0;
    private int b = 0;

    private String sign;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        final Button resultOperationButton = (Button)findViewById(R.id.resultOperation);



        resultOperationButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                EditText editText = (EditText)findViewById(R.id.editText);

                result = editText.getText().toString();

                Log.i("result : ", result);
                //1 + 1

                //데이터 분류

                Integer.parseInt(result);


                //a =

                // sign

                // b =


                switch (sign){
                    case "+" :
                        System.out.println(a + b);
                        break;
                    case "-":
                        System.out.println(a - b);
                }

            }
        });






    }//end onCreate

}
