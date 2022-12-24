package com.example.flightapp;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;

public class ActivityDocuments extends AppCompatActivity {

    private ImageButton button_account_info;
    private ImageButton button_flights;;
    private ImageButton button_exit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.documents);

        button_account_info = (ImageButton) findViewById(R.id.imageButtonHome_doc);
        button_account_info.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                account_action();
            }
        });

        button_flights = (ImageButton) findViewById(R.id.imageButtonFlight);
        button_flights.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                all_flights_action();
            }
        });

        button_exit = (ImageButton) findViewById(R.id.imageButtonSettings);
        button_exit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                exit_action();
            }
        });
    }
    public void account_action() {
        Intent intent = new Intent(this, ActivityPersonalAccount.class);
        startActivity(intent);
    }

    public void all_flights_action() {
        Intent intent = new Intent(this, ActivityFlights.class);
        startActivity(intent);
    }

    public void exit_action() {
        Intent intent = new Intent(this, MainActivity.class);
        startActivity(intent);
    }
}