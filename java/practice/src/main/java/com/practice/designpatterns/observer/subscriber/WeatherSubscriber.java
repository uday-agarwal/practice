package com.practice.designpatterns.observer.subscriber;

import java.util.concurrent.Flow;

import com.practice.designpatterns.observer.publisher.WeatherData;
import com.practice.designpatterns.observer.publisher.WeatherPublisher;

public class WeatherSubscriber implements Flow.Subscriber<WeatherData> {
  private Flow.Subscription subscription;
  private int messagesRead;

  public WeatherSubscriber(WeatherPublisher publisher) {
    publisher.subscribe(this);
  }

  public void startListening() {
    subscription.request(1);
  }

  public void stopListening() {
    subscription.cancel();
  }

  @Override
  public void onSubscribe(Flow.Subscription subscription) {
    System.out.println("First consumer: subscribed!");
    this.subscription = subscription;
    subscription.request(1);
  }

  @Override
  public void onNext(WeatherData item) {
    messagesRead++;
    System.out.println("First subscriber: Got a new data point.");
    System.out.println("First property: " + item.getFirstProperty());
    System.out.println("Second property: " + item.getSecondProperty());

    if (messagesRead > 100)
      return;

    subscription.request(2);
  }

  @Override
  public void onError(Throwable throwable) {
    System.err.println("Received exception: " + throwable.getMessage());
  }

  @Override
  public void onComplete() {
    System.out.println("First subscriber: onComplete.");
  }

}
