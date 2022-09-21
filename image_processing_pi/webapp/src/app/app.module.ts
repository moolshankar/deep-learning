import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';

import { VisitorService } from './visitor.service';

import { AppComponent } from './app.component';
import { ScanComponent } from './scan/scan.component';
import { RegisterVisitorComponent } from './register-visitor/register-visitor.component';
import { DisplayInfoComponent } from './display-info/display-info.component';

@NgModule({
  declarations: [
    AppComponent,
    ScanComponent,
    RegisterVisitorComponent,
    DisplayInfoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [VisitorService],
  bootstrap: [AppComponent]
})
export class AppModule { }
