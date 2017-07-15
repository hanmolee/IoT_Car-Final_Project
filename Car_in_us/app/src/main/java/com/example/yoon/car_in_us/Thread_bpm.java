package com.example.yoon.car_in_us;


import android.app.Activity;
import android.os.Handler;

/**
 * Created by yoon on 17. 6. 21.
 */

public class Thread_bpm extends Thread {


    private Handler handler = new Handler();  //전역변수 - 앱이 동작한 순간에 메모리에 잡힘

    private Handler handler2;


    public Thread_bpm() {     // 생성자
        handler2 = new Handler();  //지역변수
    }



}