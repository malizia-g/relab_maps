import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { MapComponent } from './map/map.component';
import { FormsModule } from '@angular/forms';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { AgmCoreModule, GoogleMapsAPIWrapper } from '@agm/core';


@NgModule({
  declarations: [
    AppComponent,
    MapComponent
  ],
  imports: [
    BrowserModule,
    BrowserModule,
    AgmCoreModule.forRoot({apiKey: 'AIzaSyAFlR30N1paHO3FsTgoPOetrw2P1xZV028'}), // <---
    FormsModule, // <---
    NgbModule// <---
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
