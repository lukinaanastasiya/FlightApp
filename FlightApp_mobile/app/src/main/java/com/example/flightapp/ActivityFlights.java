package com.example.flightapp;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;

import java.util.ArrayList;

public class ActivityFlights extends AppCompatActivity {

    ArrayList<State> states = new ArrayList<State>();

    private ImageButton button_account_info;
    private ImageButton button_documents;
    private ImageButton button_exit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_flights);
        // начальная инициализация списка
        setInitialData();
        RecyclerView recyclerView = findViewById(R.id.list);
        // создаем адаптер
        StateAdapter adapter = new StateAdapter(this, states);
        // устанавливаем для списка адаптер
        recyclerView.setAdapter(adapter);

        button_account_info = (ImageButton) findViewById(R.id.accountInfo);
        button_account_info.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                account_action();
            }
        });

        button_documents = (ImageButton) findViewById(R.id.Documents_flights);
        button_documents.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                documents_action();
            }
        });

        button_exit = (ImageButton) findViewById(R.id.Exit_flights);
        button_exit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                exit_action();
            }
        });
    }
    private void setInitialData(){
        states.add(new State ("Russia", "Moscow", "08:55", "Dec 26, 2022", "Turkey", "Istanbul", "13:40", "Dec 26, 2022"));
        states.add(new State ("Turkey", "Istanbul", "15:10", "Jan 9, 2023", "Russia", "Moscow", "19:40", "Jan 9, 2023"));
        states.add(new State ("Russia", "Moscow", "20:55", "Feb 6, 2023", "Serbia", "Belgrade", "22:05", "Feb 6, 2023"));
        states.add(new State ("Serbia", "Belgrade", "07:35", "Feb 10, 2023", "Russia", "Moscow", "12:45", "Feb 10, 2023"));
    }

    public void account_action() {
        Intent intent = new Intent(this, ActivityPersonalAccount.class);
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

}