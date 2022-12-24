package com.example.flightapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.LinearLayout;

public class ActivityPersonalAccount extends AppCompatActivity {
    private ImageButton button_flights;
    private ImageButton button_documents;
    private ImageButton button_exit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_personal_account);

        button_flights = (ImageButton) findViewById(R.id.allFlights);
        button_flights.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                all_flights_action();
            }
        });

        button_documents = (ImageButton) findViewById(R.id.Documents);
        button_documents.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                documents_action();
            }
        });

        button_exit = (ImageButton) findViewById(R.id.Exit);
        button_exit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                exit_action();
            }
        });

        LinearLayout flight_info = (LinearLayout )findViewById(R.id.flight);
        flight_info.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                flight_info_action();
            }
        });
    }
    public void all_flights_action() {
        Intent intent = new Intent(this, ActivityFlights.class);
        startActivity(intent);
    }
    public void documents_action() {
        Intent intent = new Intent(this, ActivityDocuments.class);
        startActivity(intent);
    }
    public void exit_action() {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
    public void flight_info_action() {
        Intent intent = new Intent(this, ActivityFlightInfo.class);
        startActivity(intent);
    }
}