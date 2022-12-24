package com.example.flightapp;

public class State {
    private String country_from;
    private String city_from;
    private String time_from;
    private String date_from;

    private String country_in;
    private String city_in;
    private String time_in;
    private String date_in;

    public State(
            String country_from,
            String city_from,
            String time_from,
            String date_from,
            String country_in,
            String city_in,
            String time_in,
            String date_in
    ){
        this.country_from=country_from;
        this.city_from=city_from;
        this.time_from=time_from;
        this.date_from=date_from;
        this.country_in=country_in;
        this.city_in=city_in;
        this.time_in=time_in;
        this.date_in=date_in;
    }

    public String getCountry_from() {
        return this.country_from;
    }

    public void setCountry_from(String country_from) {
        this.country_from = country_from;
    }

    public String getCity_from() {
        return this.city_from;
    }

    public void setCity_from(String city_from) {
        this.city_from = city_from;
    }

    public String getTime_from() {
        return this.time_from;
    }

    public void setTime_from(String time_from) {
        this.time_from = time_from;
    }

    public String getDate_from() {
        return this.date_from;
    }

    public void setDate_from(String date_from) {
        this.date_from = date_from;
    }

    public String getCountry_in() {
        return this.country_in;
    }

    public void setCountry_in(String country_in) {
        this.country_in = country_in;
    }

    public String getCity_in() {
        return this.city_in;
    }

    public void setCity_in(String city_in) {
        this.city_in = city_in;
    }

    public String getTime_in() {
        return this.time_in;
    }

    public void setTime_in(String time_in) {
        this.time_in = time_in;
    }

    public String getDate_in() {
        return this.date_in;
    }

    public void setDate_in(String date_in) {
        this.date_in = date_in;
    }
}
