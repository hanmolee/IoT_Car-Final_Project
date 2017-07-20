package iot.car.webstreamviewer;

import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;

import org.json.JSONArray;
import org.json.JSONObject;

import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

public class MainActivity extends AppCompatActivity {

    private WebView mWebView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        mWebView = (WebView) findViewById(R.id.activity_webview);
        mWebView.getSettings().setJavaScriptEnabled(true);
        mWebView.loadUrl("http://192.168.0.14:3001/blinkers");
        mWebView.setWebViewClient(new WebViewClient());

        GetWinkerOrientation task = new GetWinkerOrientation();
        task.execute();
    }

    private class GetWinkerOrientation extends AsyncTask<Void, String, String> {

        private final String url = "http://192.168.0.14:3001/blinkers";
        final String LEFT_URL = "http://192.168.0.17:8080/stream_simple.html";
        final String RIGHT_URL = "http://192.168.0.9:8080/stream_simple.html";

        OkHttpClient client;
        Request request;
        Response response;
        String message;
        JSONArray outerArray, innerArray;
        JSONObject json;

        @Override
        protected void onPreExecute() {
            super.onPreExecute();
        }

        @Override
        protected String doInBackground(Void... values) {
            while (!isCancelled()) {
                try {
                    client = new OkHttpClient();
                    request = new Request.Builder().url(url).build();
                    response = client.newCall(request).execute();
                    message = response.body().string();

                    try {
                        outerArray = new JSONArray(message);
                        innerArray = outerArray.getJSONArray(0);
                        json = innerArray.getJSONObject(0);
                        String winkerValue = json.get("winker").toString();

                        publishProgress(winkerValue);
                    } catch (Exception e) {
                        publishProgress("C");
                    }

                    Thread.sleep(1200);
                } catch(Exception e) {
                    e.printStackTrace();
                }
            }

            return null;
        }

        @Override
        protected void onProgressUpdate(String... values) {
            switch (values[0]) {
                case "C":
                    haveToRefresh(url);
                    break;
                case "L":
                    haveToRefresh(LEFT_URL);
                    break;
                case "R":
                    haveToRefresh(RIGHT_URL);
                    break;
            }
        }

        private void haveToRefresh(String url) {
            if (!mWebView.getUrl().equals(url)) {
                mWebView.loadUrl(url);
                mWebView.setWebViewClient(new WebViewClient());
            }
        }

    }
}
