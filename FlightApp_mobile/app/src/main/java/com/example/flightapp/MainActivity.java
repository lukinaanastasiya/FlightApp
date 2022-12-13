package com.example.flightapp;

import android.os.Bundle;
import android.widget.TextView;
import okhttp3.Call;
import okhttp3.Callback;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.Response;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import java.io.IOException;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);

        OkHttpClient okHttpClient = new OkHttpClient();
        Request request = new Request.Builder().url("http://192.168.1.49:5000/all_flights/").build();

        okHttpClient.newCall(request).enqueue(new Callback() {
           @Override
           public void onFailure(@NonNull Call call, @NonNull IOException e) {
               TextView textView = findViewById(R.id.textview);
               textView.setText("connection failed");
           }
           @Override
            public void onResponse(@NonNull Call call, @NonNull Response response) throws IOException {

               TextView textView = findViewById(R.id.textview);
               textView.setText(response.body().string());

           }
        });
    }
}
