package com.example.flightapp;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
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
    private Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        setContentView(R.layout.login);
        button = (Button) findViewById(R.id.buttonLogin);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                login_action();
            }
        });

//        OkHttpClient okHttpClient = new OkHttpClient();
//        Request request = new Request.Builder().url("http://192.168.1.49:5000/all_flights/").build();
//
//        try {
//            Response response = okHttpClient.newCall(request).execute();
//            TextView textView = findViewById(R.id.textview);
//            textView.setText(response.body().string());
//        } catch (IOException e) {
//            e.printStackTrace();
//        }
    }
    public void login_action() {
        Intent intent = new Intent(this, ActivityPersonalAccount.class);
        startActivity(intent);
    }
}
