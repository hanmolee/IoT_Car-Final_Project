package com.example.yoon.car_in_us;

import android.app.Activity;
import android.os.Bundle;
import android.support.annotation.Nullable;

/**
 * Created by yoon on 17. 6. 26.
 */

public class BpmActivity extends Activity {

    @Override
    protected void onCreate(@Nullable Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.heart_activvity);

        Thread_bpm thread_bpm = new Thread_bpm();
    }

}
