package com.example.flightapp;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class StateAdapter  extends RecyclerView.Adapter<StateAdapter.ViewHolder>{

    private final LayoutInflater inflater;
    private final List<State> states;

    StateAdapter(Context context, List<State> states) {
        this.states = states;
        this.inflater = LayoutInflater.from(context);
    }
    @Override
    public StateAdapter.ViewHolder onCreateViewHolder(ViewGroup parent, int viewType) {

        View view = inflater.inflate(R.layout.item_fo_flight, parent, false);
        return new ViewHolder(view);
    }

    @Override
    public void onBindViewHolder(StateAdapter.ViewHolder holder, int position) {
        State state = states.get(position);
        holder.countryFromView.setText(state.getCountry_from());
        holder.cityFromView.setText(state.getCity_from());
        holder.timeFromView.setText(state.getTime_from());
        holder.dateFromView.setText(state.getDate_from());

        holder.countryInView.setText(state.getCountry_in());
        holder.cityInView.setText(state.getCity_in());
        holder.timeInView.setText(state.getTime_in());
        holder.dateInView.setText(state.getDate_in());
    }

    @Override
    public int getItemCount() {
        return states.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder {
        final TextView countryFromView, cityFromView, timeFromView, dateFromView,
                countryInView, cityInView, timeInView, dateInView;
        ViewHolder(View view){
            super(view);
            countryFromView = view.findViewById(R.id.country_from);
            cityFromView = view.findViewById(R.id.city_from);
            timeFromView = view.findViewById(R.id.time_from);
            dateFromView = view.findViewById(R.id.date_from);
            countryInView = view.findViewById(R.id.country_in);
            cityInView = view.findViewById(R.id.city_in);
            timeInView = view.findViewById(R.id.time_in);
            dateInView = view.findViewById(R.id.date_in);
        }
    }
}